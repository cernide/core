from core.common import auditor
from core.common.events.registry import bookmark

auditor.subscribe(bookmark.ProjectBookmarkedActorEvent)
auditor.subscribe(bookmark.ProjectUnBookmarkedActorEvent)
auditor.subscribe(bookmark.RunBookmarkedActorEvent)
auditor.subscribe(bookmark.RunUnBookmarkedActorEvent)
