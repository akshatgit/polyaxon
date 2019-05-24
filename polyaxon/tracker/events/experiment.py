import tracker

from events.registry import experiment

tracker.subscribe(experiment.ExperimentCreatedEvent)
tracker.subscribe(experiment.ExperimentUpdatedEvent)
tracker.subscribe(experiment.ExperimentDeletedEvent)
tracker.subscribe(experiment.ExperimentViewedEvent)
tracker.subscribe(experiment.ExperimentArchivedEvent)
tracker.subscribe(experiment.ExperimentRestoredEvent)
tracker.subscribe(experiment.ExperimentBookmarkedEvent)
tracker.subscribe(experiment.ExperimentUnBookmarkedEvent)
tracker.subscribe(experiment.ExperimentStoppedEvent)
tracker.subscribe(experiment.ExperimentResumedEvent)
tracker.subscribe(experiment.ExperimentRestartedEvent)
tracker.subscribe(experiment.ExperimentCopiedEvent)
tracker.subscribe(experiment.ExperimentNewStatusEvent)
tracker.subscribe(experiment.ExperimentNewMetricEvent)
tracker.subscribe(experiment.ExperimentSucceededEvent)
tracker.subscribe(experiment.ExperimentFailedEvent)
tracker.subscribe(experiment.ExperimentDoneEvent)
tracker.subscribe(experiment.ExperimentResourcesViewedEvent)
tracker.subscribe(experiment.ExperimentLogsViewedEvent)
tracker.subscribe(experiment.ExperimentOutputsDownloadedEvent)
tracker.subscribe(experiment.ExperimentStatusesViewedEvent)
tracker.subscribe(experiment.ExperimentJobsViewedEvent)
tracker.subscribe(experiment.ExperimentMetricsViewedEvent)
tracker.subscribe(experiment.ExperimentDeletedTriggeredEvent)
tracker.subscribe(experiment.ExperimentStoppedTriggeredEvent)
tracker.subscribe(experiment.ExperimentResumedTriggeredEvent)
tracker.subscribe(experiment.ExperimentRestartedTriggeredEvent)
tracker.subscribe(experiment.ExperimentCopiedTriggeredEvent)
