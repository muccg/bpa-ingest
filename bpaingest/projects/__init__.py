from .base.ingest import (
    BASEAmpliconsMetadata,
    BASEMetagenomicsMetadata,
    BASEAmpliconsControlMetadata,
    BASESiteImagesMetadata)
from .gbr.ingest import GbrAmpliconsMetadata
from .mm.ingest import (
    MarineMicrobesGenomicsAmplicons16SMetadata,
    MarineMicrobesGenomicsAmpliconsA16SMetadata,
    MarineMicrobesGenomicsAmplicons18SMetadata,
    MarineMicrobesGenomicsAmplicons16SControlMetadata,
    MarineMicrobesGenomicsAmpliconsA16SControlMetadata,
    MarineMicrobesGenomicsAmplicons18SControlMetadata,
    MarineMicrobesMetagenomicsMetadata,
    MarineMicrobesMetatranscriptomeMetadata)
from .sepsis.ingest import (
    SepsisGenomicsMiseqMetadata,
    SepsisTranscriptomicsHiseqMetadata,
    SepsisGenomicsPacbioMetadata,
    SepsisMetabolomicsLCMSMetadata,
    SepsisMetabolomicsGCMSMetadata,
    SepsisProteomicsMS1QuantificationMetadata,
    SepsisProteomicsSwathMSMetadata,
    SepsisProteomicsProteinDatabaseMetadata,
    SepsisProteomicsSwathMSPoolMetadata,
    SepsisProteomicsSwathMSCombinedSampleMetadata,
    SepsisProteomicsAnalysedMetadata,
    SepsisTranscriptomicsAnalysedMetadata,
    SepsisMetabolomicsAnalysedMetadata,
    SepsisGenomicsAnalysedMetadata)
from .stemcells.ingest import (
    StemcellsTranscriptomeMetadata,
    StemcellsSmallRNAMetadata,
    StemcellsSingleCellRNASeqMetadata,
    StemcellsMetabolomicsMetadata,
    StemcellsProteomicsMetadata,
    StemcellsProteomicsPoolMetadata,
    StemcellsProteomicsAnalysedMetadata,
    StemcellsMetabolomicsAnalysedMetadata)
from .wheat_cultivars.ingest import WheatCultivarsMetadata
from .wheat_pathogens_genomes.ingest import WheatPathogensGenomesMetadata
from .omg.ingest import (
    OMG10XProcessedIlluminaMetadata,
    OMG10XRawIlluminaMetadata,
    OMG10XRawMetadata,
    OMGExonCaptureMetadata,
    OMGGenomicsHiSeqMetadata)


class ProjectInfo:
    projects = {
#        'base': [
#            BASEAmpliconsMetadata,
#            BASEAmpliconsControlMetadata,
#            BASEMetagenomicsMetadata,
#            BASESiteImagesMetadata,
#        ],
#        'gbr': [
#            GbrAmpliconsMetadata,
#        ],
#        'marine-microbes': [
#            MarineMicrobesGenomicsAmplicons16SMetadata,
#            MarineMicrobesGenomicsAmpliconsA16SMetadata,
#            MarineMicrobesGenomicsAmplicons18SMetadata,
#            MarineMicrobesGenomicsAmplicons16SControlMetadata,
#            MarineMicrobesGenomicsAmpliconsA16SControlMetadata,
#            MarineMicrobesGenomicsAmplicons18SControlMetadata,
#            MarineMicrobesMetagenomicsMetadata,
#            MarineMicrobesMetatranscriptomeMetadata,
#        ],
#        'omg': [
#            OMG10XRawIlluminaMetadata,
#            OMG10XRawMetadata,
#            OMG10XProcessedIlluminaMetadata,
#            OMGExonCaptureMetadata,
#            OMGGenomicsHiSeqMetadata,
#        ],
        'sepsis': [
            SepsisGenomicsMiseqMetadata,
            SepsisGenomicsPacbioMetadata,
            SepsisGenomicsAnalysedMetadata,
            SepsisTranscriptomicsAnalysedMetadata,
            SepsisTranscriptomicsHiseqMetadata,
            SepsisMetabolomicsLCMSMetadata,
            SepsisMetabolomicsGCMSMetadata,
            SepsisMetabolomicsAnalysedMetadata,
            SepsisProteomicsMS1QuantificationMetadata,
            SepsisProteomicsSwathMSMetadata,
            SepsisProteomicsSwathMSCombinedSampleMetadata,
            SepsisProteomicsSwathMSPoolMetadata,
            SepsisProteomicsAnalysedMetadata,
            SepsisProteomicsProteinDatabaseMetadata,
        ],
#        'stemcells': [
#            StemcellsTranscriptomeMetadata,
#            StemcellsSmallRNAMetadata,
#            StemcellsSingleCellRNASeqMetadata,
#            StemcellsMetabolomicsMetadata,
#            StemcellsProteomicsMetadata,
#            StemcellsProteomicsPoolMetadata,
#            StemcellsProteomicsAnalysedMetadata,
#            StemcellsMetabolomicsAnalysedMetadata,
#        ],
#        'wheat-cultivars': [
#            WheatCultivarsMetadata,
#        ],
#        'wheat-pathogens': [
#            WheatPathogensGenomesMetadata,  # the first half of wheat pathogens
#        ],
    }

    def __init__(self):
        self.metadata_info = self._build_metadata_info()

    def _build_metadata_info(self):
        info = []
        slugs = set()
        for project_name, classes in ProjectInfo.projects.items():
            for cls in classes:
                if not getattr(cls, 'parse_spreadsheet', None):
                    continue
                class_info = dict((t, getattr(cls, t, None)) for t in ('omics', 'technology', 'organization'))
                class_info.update(dict((t, getattr(cls, t, False)) for t in ('analysed', 'pool')))
                class_info['project'] = project_name
                class_info['cls'] = cls
                class_info['slug'] = slug = self._make_slug(class_info)
                # ensure that 'slug' is unique
                assert(slug not in slugs)
                slugs.add(slug)
                info.append(class_info)
        return info

    def _make_slug(self, class_info):
        nm_parts = [class_info[t] for t in ('project', 'omics', 'technology')]
        if class_info['analysed']:
            nm_parts.append('analysed')
        if class_info['pool']:
            nm_parts.append('pool')
        return '-'.join(filter(None, nm_parts))

    def cli_options(self):
        return dict((t['slug'], t['cls']) for t in self.metadata_info)
