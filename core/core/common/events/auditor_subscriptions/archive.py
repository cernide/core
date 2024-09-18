from core.common import auditor
from core.common.events.registry import archive

auditor.subscribe(archive.ProjectArchivedActorEvent)
auditor.subscribe(archive.ProjectRestoredActorEvent)
auditor.subscribe(archive.RunArchivedActorEvent)
auditor.subscribe(archive.RunRestoredActorEvent)
