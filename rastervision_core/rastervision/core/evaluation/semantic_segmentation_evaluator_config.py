from typing import TYPE_CHECKING, Iterable, Optional, Tuple
from os.path import join

from rastervision.pipeline.config import register_config
from rastervision.core.evaluation.classification_evaluator_config import (
    ClassificationEvaluatorConfig)
from rastervision.core.evaluation.semantic_segmentation_evaluator import (
    SemanticSegmentationEvaluator)

if TYPE_CHECKING:
    from rastervision.core.data import ClassConfig


def ss_evaluator_config_upgrader(cfg_dict: dict, version: int) -> dict:
    if version < 3:
        try:
            # removed in version 3
            del cfg_dict['vector_output_uri']
        except KeyError:
            pass
    return cfg_dict


@register_config(
    'semantic_segmentation_evaluator', upgrader=ss_evaluator_config_upgrader)
class SemanticSegmentationEvaluatorConfig(ClassificationEvaluatorConfig):
    def build(self,
              class_config: 'ClassConfig',
              scene_group: Optional[Tuple[str, Iterable[str]]] = None
              ) -> SemanticSegmentationEvaluator:
        if scene_group is None:
            output_uri = self.get_output_uri()
            vector_output_uri = self.get_vector_output_uri()
        else:
            group_name, _ = scene_group
            output_uri = self.get_output_uri(group_name)
            vector_output_uri = self.get_vector_output_uri(group_name)

        evaluator = SemanticSegmentationEvaluator(class_config, output_uri,
                                                  vector_output_uri)
        return evaluator

    def get_vector_output_uri(self,
                              scene_group_name: Optional[str] = None) -> str:
        if scene_group_name is None:
            return join(self.output_uri, 'vector-eval.json')
        return join(self.output_uri, scene_group_name, 'vector-eval.json')
