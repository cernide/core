from django.contrib.admin import site
from django.contrib.auth.admin import UserAdmin

from core.db.administration.artifacts import ArtifactAdmin
from core.db.administration.projects import ProjectAdmin
from core.db.administration.runs import RunLightAdmin
from core.db.defs import Models

site.register(Models.User, UserAdmin)
site.register(Models.Artifact, ArtifactAdmin)
site.register(Models.Project, ProjectAdmin)
site.register(Models.Run, RunLightAdmin)
