from core.common import conf
from core.common.options.registry import containers

conf.subscribe(containers.PolyaxonInitContainer)
conf.subscribe(containers.PolyaxonSidecarContainer)
