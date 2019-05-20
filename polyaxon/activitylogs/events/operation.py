import activitylogs

from event_manager.events import operation

activitylogs.subscribe(operation.OperationCreatedEvent)
activitylogs.subscribe(operation.OperationUpdatedEvent)
activitylogs.subscribe(operation.OperationViewedEvent)
activitylogs.subscribe(operation.OperationArchivedEvent)
activitylogs.subscribe(operation.OperationRestoredEvent)
activitylogs.subscribe(operation.OperationDeletedTriggeredEvent)
