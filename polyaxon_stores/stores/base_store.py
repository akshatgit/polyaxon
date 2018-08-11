# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from polyaxon_stores.exceptions import PolyaxonStoresException
from polyaxon_stores.utils import get_from_env


class Store(object):
    """
    A base store interface.
    """
    _LOCAL_STORE = 'local'
    _AZURE_STORE = 'azure'
    _S3_STORE = 's3'
    _GCS_STORE = 'gcs'
    _STORE_TYPES = {_LOCAL_STORE, _AZURE_STORE, _S3_STORE, _GCS_STORE}

    STORE_TYPE = None

    @classmethod
    def get_store(cls, store_type=None):
        store_type = store_type or get_from_env(['POLYAXON_STORE'])
        # We assume that `None` refers to local store as well
        store_type = cls._LOCAL_STORE if store_type is None else store_type
        if store_type not in cls._STORE_TYPES:
            raise PolyaxonStoresException(
                'Received an unrecognised store type `{}`.'.format(store_type))

        if store_type == cls._LOCAL_STORE:
            from polyaxon_stores.stores.local_store import LocalStore
            return LocalStore()
        if store_type == cls._AZURE_STORE:
            from polyaxon_stores.stores.azure_store import AzureStore
            return AzureStore()
        if store_type == cls._S3_STORE:
            from polyaxon_stores.stores.s3_store import S3Store
            return S3Store()
        if store_type == cls._GCS_STORE:
            from polyaxon_stores.stores.gcs_store import GCSStore
            return GCSStore()

    def download_file(self, *args, **kwargs):
        raise NotImplementedError

    def download_dir(self, *args, **kwargs):
        raise NotImplementedError

    def upload_file(self, *args, **kwargs):
        raise NotImplementedError

    def upload_dir(self, *args, **kwargs):
        raise NotImplementedError
