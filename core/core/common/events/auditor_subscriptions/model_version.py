from core.common import auditor
from core.common.events.registry import model_version

auditor.subscribe(model_version.ModelVersionDeletedEvent)
auditor.subscribe(model_version.ModelVersionCreatedActorEvent)
auditor.subscribe(model_version.ModelVersionUpdatedActorEvent)
auditor.subscribe(model_version.ModelVersionViewedActorEvent)
auditor.subscribe(model_version.ModelVersionDeletedActorEvent)
auditor.subscribe(model_version.ModelVersionTransferredActorEvent)
auditor.subscribe(model_version.ModelVersionNewStageEvent)
