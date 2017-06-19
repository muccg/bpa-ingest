from __future__ import print_function

from unipath import Path

from ...util import make_logger
from ...abstract import BaseMetadata

logger = make_logger(__name__)


class WheatPathogensTranscriptMetadata(BaseMetadata):
    metadata_urls = ['https://downloads-qcif.bioplatforms.com/bpa/wheat_pathogens/tracking/']
    organization = 'bpa-wheat-pathogens-transcript'
    auth = ('marine', 'mm')

    def __init__(self, metadata_path):
        super(WheatPathogensTranscriptMetadata, self).__init__()
        self.path = Path(metadata_path)

    def _get_packages(self):
        return []

    def _get_resources(self):
        return []
