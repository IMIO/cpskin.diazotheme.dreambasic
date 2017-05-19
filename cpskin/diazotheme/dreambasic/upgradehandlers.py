# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger('cpskin.diazotheme.dreambasic')


def upgrade_to_less(context):
    context.runImportStepFromProfile(
        'profile-cpskin.diazotheme.dreambasic:default',
        'lessregistry'
    )
    logger.info('LESS files installed and configurations done !')
