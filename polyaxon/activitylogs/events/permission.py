import activitylogs

from events.registry import permission

activitylogs.subscribe(permission.PermissionProjectDeniedEvent)
activitylogs.subscribe(permission.PermissionRepoDeniedEvent)
activitylogs.subscribe(permission.PermissionExperimentGroupDeniedEvent)
activitylogs.subscribe(permission.PermissionExperimentDeniedEvent)
activitylogs.subscribe(permission.PermissionTensorboardDeniedEvent)
activitylogs.subscribe(permission.PermissionNotebookDeniedEvent)
activitylogs.subscribe(permission.PermissionBuildJobDeniedEvent)
activitylogs.subscribe(permission.PermissionExperimentJobDeniedEvent)
activitylogs.subscribe(permission.PermissionClusterDeniedEvent)
activitylogs.subscribe(permission.PermissionUserRoleEvent)
