from ...util import make_logger
import re

logger = make_logger(__name__)

tenxtar_filename_re = re.compile(r"""(?P<basename>.*)\.tar""")

EXON_FILENAME_PATTERN = r"""
    (?P<bpa_library_id>\d{4,6})_
    (?P<flow_cell_id>\w{9,10})_
    (?P<index>[G|A|T|C|-]*)_
    (?P<runsamplenum>S\d*)_
    (?P<lane>L\d{3})_
    (?P<read>[R|I][1|2])_
    (?P<flowcellindex>\d{3})
    \.fastq\.gz$
"""
exon_filename_re = re.compile(EXON_FILENAME_PATTERN, re.VERBOSE)

WHOLE_GENOME_FILENAME_PATTERN = r"""
    (?P<bpa_library_id>\d{4,6})_
    (?P<flow_cell_id>\w{9,10})_
    (?P<index>[G|A|T|C|-]*)_
    (?P<runsamplenum>S\d*)_
    (?P<lane>L\d{3})_
    (?P<read>[R|I][1|2])_
    (?P<flowcellindex>\d{3})
    \.fastq\.gz$
"""
whole_genome_filename_re = re.compile(WHOLE_GENOME_FILENAME_PATTERN, re.VERBOSE)

NOVASEQ_FILENAME_PATTERN = r"""
    (?P<bpa_library_id>\d{4,6})_
    (?P<voucher_id>\w+)_
    (pool_)?
    (?P<flow_cell_id>\w{9,10})_
    (?P<index>[G|A|T|C|-]*)_
    (?P<lane>L\d{3})_
    (?P<read>[R|I][1|2])
    \.fastq\.gz
"""
novaseq_filename_re = re.compile(NOVASEQ_FILENAME_PATTERN, re.VERBOSE)

TENXFASTQ_FILENAME_PATTERN = r"""
    (?P<bpa_sample_id>\d{4,6})_
    (?P<runsamplenum>S\d*)_
    (?P<lane>L\d{3})_
    (?P<read>[R|I][1|2])_
    001\.fastq\.gz$
"""
tenxfastq_filename_re = re.compile(TENXFASTQ_FILENAME_PATTERN, re.VERBOSE)

TENX_RAW_XLSX_FILENAME_PATTERN = r"""
    (?P<bpa_sample_id>\d{4,6})_
    OMG_
    (?P<facility>UNSW)_
    (?P<flow_id>\w+)
    _metadata.xlsx$
"""
tenx_raw_xlsx_filename_re = re.compile(TENX_RAW_XLSX_FILENAME_PATTERN, re.VERBOSE)

# For the short read data we should follow the new BPA file naming protocol that Mabel circulated fairly recently - I'm not sure if it reached you, but I've attached it here. Essentially it is:
# <BPA sample ID>_<flowcell ID>_<index sequence>_<sample number>_<lane>_<read>_001.fastq.gz
# If there is a missing field (eg if you have no index sequences), keep the field in the filename but use Ns instead.
HISEQ_FILENAME_PATTERN = r"""
    (?P<bpa_sample_id>\d{4,6})_
    (?P<flow_cell_id>\w{9})_
    (?P<index>[G|A|T|C|-]*|N)_
    (?P<sample_number>S\d)_
    (?P<lane>L\d{3})_
    (?P<read>[R|I][1|2])_001\.fastq\.gz
"""
hiseq_filename_re = re.compile(HISEQ_FILENAME_PATTERN, re.VERBOSE)

sample_sheet_re = re.compile(r"^SampleSheet\.csv$")

DDRAD_FASTQ_FILENAME_PATTERN = r"""
    (?P<bpa_dataset_id>\d{4,6})_
    (?P<flowcell_id>\w{9})_
    (?P<index>[G|A|T|C|-]*|N)_
    (?P<lane>L\d{3})_
    (?P<read>[R|I][1|2])\.fastq\.gz
"""
ddrad_fastq_filename_re = re.compile(DDRAD_FASTQ_FILENAME_PATTERN, re.VERBOSE)

DDRAD_METADATA_SHEET_PATTERN = r"""
    OMG_
    NGS_
    AGRF_
    (?P<bpa_dataset_id>\d{4,6})_
    (?P<flowcell_id>\w{9})
    _metadata\.xlsx
"""
ddrad_metadata_sheet_re = re.compile(DDRAD_METADATA_SHEET_PATTERN, re.VERBOSE)

DDRAD_METADATA_SHEET_2_PATTERN = r"""
    OMG_
    NGS_
    (?P<flowcell_id>\w{9})_
    library_metadata_
    (?P<bpa_dataset_id>\d{4,6})
    \.xlsx
"""
ddrad_metadata_sheet_2_re = re.compile(DDRAD_METADATA_SHEET_2_PATTERN, re.VERBOSE)

PACBIO_PATTERN = r"""
    (?P<bpa_library_id>\d{4,6})_
    (?P<facility>UNSW)_
    PAC_
    (?P<run_date>\d{8})_
    (?P<run_code>.{3})
    \.tar\.gz
"""
pacbio_filename_re = re.compile(PACBIO_PATTERN, re.VERBOSE)

ONT_PROMETHION_PATTERN = r"""
    (?P<bpa_library_id>\d{4,6})_
    (?P<flowcell_id>PA[DE]\d{5})_
    OMG_
    (?P<facility_id>(AGRF))_
    ONTPromethion_
    (?P<archive_type>\w+)
    \.tar
"""
ont_promethion_re = re.compile(ONT_PROMETHION_PATTERN, re.VERBOSE)

TRANSCRIPTOMICS_NEXTSEQ_FASTQ_FILENAME_PATTERN = r"""
    (?P<bpa_library_id>\d{4,6})_
    (?P<flowcell_id>\w{9})_
    (?P<index>[G|A|T|C|-]*|N)_
    (?P<runsamplenum>S\d*)_
    (?P<lane>L\d{3})_
    (?P<read>[R|I][1|2])
    _001\.fastq\.gz
"""
transcriptomics_nextseq_fastq_filename_re = re.compile(
    TRANSCRIPTOMICS_NEXTSEQ_FASTQ_FILENAME_PATTERN, re.VERBOSE
)

PACBIO_SECONDARY_PATTERN = r"""
    (?P<bpa_library_id>\d{4,6})_
    (?P<folder_name>Scras_dunnart_assem1\.0)_
    pb-ont-illsr_flyeassem_red-rd-scfitr2_
    pil2xwgs2_
    60chr
    \.fasta
"""
pacbio_secondary_filename_re = re.compile(PACBIO_SECONDARY_PATTERN, re.VERBOSE)

PACBIO_SECONDARY_RAW_PATTERN = r"""
    (?P<bpa_sample_id>\d{4,6})_
    m\d{4,6}_
    (?P<run_date>\d{6})_
    \d{4,6}
    \.subreads
    \.bam
"""
pacbio_secondary_raw_filename_re = re.compile(PACBIO_SECONDARY_RAW_PATTERN, re.VERBOSE)
