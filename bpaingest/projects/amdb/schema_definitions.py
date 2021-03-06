from glob import glob
import pandas
from numpy import nan

from ...util import one


class AustralianMicrobiomeSchema:
    metadata_urls = [
        "https://github.com/AusMicrobiome/contextualdb_doc/raw/2.0.2/db_schema_definitions/db_schema_definitions.xlsx"
    ]
    name = "amd-schema_definitions"
    sheet_name = "2.0.2"
    source_pattern = "/*.xlsx"

    def __init__(self, logger, path):
        self._logger = logger
        self.path_dir = path
        self.source_path = one(glob(path + self.source_pattern))
        self.schema_definitions = None

    def get_schema_definitions(self, use_cols=None, pandas_format=None):
        if self.schema_definitions is None:
            if use_cols is None:
                use_cols = ["Field", "dType", "AM_enviro", "Units_Definition", "Units"]
            if pandas_format is None:
                pandas_format = "records"
            schema_as_dataframes = pandas.read_excel(
                self.source_path, sheet_name=0, usecols=use_cols
            )
            self.schema_definitions = schema_as_dataframes.to_dict(pandas_format)
        return self.schema_definitions

    # basic: won't distinguish complex comparisons such as unit functions(e.g., date-time)
    # or badly written utf8 codes in incoming sheet such as `micro` symbol'
    def validate_schema_units(self, context_field_specs):
        self._logger.info("comparing units...")
        missing_values = [None, nan]
        schema_definitions = {
            s["Field"]: s["Units"] for s in self.get_schema_definitions()
        }
        context_definitions = {c.column_name: c.units for c in context_field_specs}
        for s in schema_definitions:
            if s not in context_definitions:
                raise Exception(
                    f"Schema definition column: {s} not found in context class"
                )
        for c in context_definitions:
            if c not in schema_definitions:
                raise Exception(f"Context Class column: {c} not found in schema class")
            if (
                schema_definitions[c] in missing_values
                and context_definitions[c] in missing_values
            ):
                continue
            if schema_definitions[c] != context_definitions[c]:
                self._logger.warn(
                    f"Units in Context column: {c} is {context_definitions[c]}, but in the schema it is: {schema_definitions[c]}"
                )
