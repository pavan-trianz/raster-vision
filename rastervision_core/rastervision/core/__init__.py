# flake8: noqa

import rastervision.pipeline
from rastervision.core.box import *
from rastervision.core.data_sample import *
from rastervision.core.predictor import *
from rastervision.core.raster_stats import *

# We just need to import anything that contains a Config, so that all
# the register_config decorators will be called which add Configs to the
# registry.
import rastervision.core.backend
import rastervision.core.data
import rastervision.core.rv_pipeline
import rastervision.core.evaluation


def register_plugin(registry):
    registry.set_plugin_version('rastervision.core', 3)
    registry.set_plugin_aliases('rastervision.core', ['rastervision2.core'])
    from rastervision.core.cli import predict
    registry.add_plugin_command(predict)
