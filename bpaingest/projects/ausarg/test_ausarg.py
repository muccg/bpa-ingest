from bpaingest.projects.ausarg.files import (
    illumina_fastq_re,
    metadata_sheet_re,
    ont_promethion_re,
    pacbio_hifi_filename_re,
    pacbio_hifi_metadata_sheet_re,
    exon_filename_re,
    illumina_hic_re,
)


def test_raw_xlsx_filename_re():
    filenames = [
        "AusARG_UNSW_HH2JJBGXG_metadata.xlsx",
    ]
    for filename in filenames:
        assert metadata_sheet_re.match(filename) is not None


def test_fastq_filename_re():
    filenames = [
        "350728_AusARG_UNSW_HH2JJBGXG_CCTGAACT-CCAACAGA_S9_L001_R1_001.fastq.gz",
        "350733_AusARG_UNSW_HGGKCBGXH_ATATGCAT-CCAGGCAC_S5_R2_001.fastq.gz",
        "350734_AusARG_UNSW_HGGKCBGXH_ATGGCGCC-AGGCCGTG_S6_R1_001.fastq.gz",
    ]
    for filename in filenames:
        assert illumina_fastq_re.match(filename) is not None


def test_ont_promethion_re():
    filenames = [
        "350767_PAG18256_AusARG_RamaciottiGarvan_ONTPromethION_fast5_fail.tar",
        "350767_PAG18256_AusARG_RamaciottiGarvan_ONTPromethION_fast5_pass.tar",
        "350767_PAG18256_AusARG_RamaciottiGarvan_ONTPromethION_fastq_fail.tar",
        "350767_PAG18256_AusARG_RamaciottiGarvan_ONTPromethION_fastq_pass.tar",
        "350767_PAG18256_AusARG_RamaciottiGarvan_ONTPromethION_plots.tar",
        "350767_PAG18256_AusARG_RamaciottiGarvan_ONTPromethION_sequencing_summary.tar",
        "350751_PAG89453_AusARG_RamaciottiGarvan_ONTPromethION_plots.html",
        "350751_PAG89453_AusARG_RamaciottiGarvan_ONTPromethION_sequencing_summary.txt",
    ]
    for filename in filenames:
        assert ont_promethion_re.match(filename) is not None


def test_pacbio_hifi():
    filenames = [
        "355356_AusARG_AGRF_PacBio_DA052899_ccs_statistics.csv",
        "355356_AusARG_AGRF_PacBio_DA052899_final.consensusreadset.xml",
        "355356_AusARG_AGRF_PacBio_DA052899.ccs.bam",
        "355356_AusARG_AGRF_PacBio_DA052899.subreads.bam",
        "355356_AusARG_AGRF_PacBio_DA052899.pdf",
        "350719_AusARG_AGRF_PacBio_DA052894_DA052873.ccs.bam",
        "350719_AusARG_AGRF_PacBio_DA052894_DA052873_ccs_statistics.csv",
        "350719_AusARG_AGRF_PacBio_DA052894_DA052873_final.consensusreadset.xml",
        "349741_AusARG_AGRF_PacBio_DA043673.pdf",
        "350719_AusARG_AGRF_PacBio_DA052873.pdf",
        "350719_AusARG_AGRF_PacBio_DA052894.pdf",
        "349741_AusARG_AGRF_PacBio_DA043669.pdf",
        "350837_AusARG_AGRF_DA087270.HiFi_qc.pdf",
    ]

    for filename in filenames:
        assert pacbio_hifi_filename_re.match(filename) is not None


def test_pacbio_hifi_metadata_sheet():
    filenames = [
        "355356_AusARG_AGRF_PacBio_DA052899_metadata.xlsx",
        "350719_AusARG_AGRF_PacBio_DA052894_DA052873_metadata.xlsx",
        "350837_AusARG_AGRF_DA087270.metadata.xlsx",
    ]

    for filename in filenames:
        assert pacbio_hifi_metadata_sheet_re.match(filename) is not None


def test_exon():
    filenames = [
        "349779_AHHVV2AFX2_TACGCCAAGT_S1_L001_R1_001.fastq.gz",
        "349779_AHHVV2AFX2_TACGCCAAGT_S1_L001_R2_001.fastq.gz",
        "349779_AHHVV2AFX2_TACGCCAAGT_S1_L002_R1_001.fastq.gz",
    ]

    for filename in filenames:
        assert exon_filename_re.match(filename) is not None


def test_illumina_hic():
    filenames = [
        "350764_AusARG_BRF_DD2M2_TGACCA_S2_L001_R1_001.fastq.gz",
        "350769_AusARG_BRF_DD2M2_CAGATC_S5_L001_R1_001.fastq.gz",
        "350821_AusARG_BRF_DD2M2_CGATGT_S1_L001_R1_001.fastq.gz",
        "350752_AusARG_BRF_HCN7WDRXY_S4_L001_R1_001.fastq.gz",
        "350752_AusARG_BRF_HCN7WDRXY_S4_L001_R2_001.fastq.gz",
        "350752_AusARG_BRF_HCN7WDRXY_S4_L002_R1_001.fastq.gz",
    ]
    for filename in filenames:
        assert illumina_hic_re.match(filename) is not None
