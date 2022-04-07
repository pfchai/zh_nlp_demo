# -*- coding: utf-8 -*-

import argparse

from zh_nlp_demo.keras.data.dataset.weibo2018 import WeiBo2018
from zh_nlp_demo.keras.data.dataset.cail2018 import CAIL2018


def create_parser(description='文本分类'):
    support_dataset = (
        'weibo2018', 'cal2018_accu_e', 'cal2018_accu_fs',
        'cal2018_ra_e', 'cal2018_ra_fs', 'cal2018_toi_e', 'cal2018_toi_fs'
    )
    parser = argparse.ArgumentParser(description='基于LSTM的文本分类')
    parser.add_argument(
        '--dataset', type=str, default='weibo2018',
        choices=support_dataset, help='指定数据集'
    )
    parser.add_argument('--do_train', action='store_true', default=False)
    parser.add_argument('--do_test', action='store_true', default=False)
    return parser


def create_dataset(args):
    if args.dataset == 'weibo2018':
        dataset = WeiBo2018()
    elif args.dataset == 'cal2018_accu_e':
        dataset = CAIL2018(task_name='accusation', sub_data='exercise')
    elif args.dataset == 'cal2018_accu_fs':
        dataset = CAIL2018(task_name='accusation', sub_data='first_stage')
    elif args.dataset == 'cal2018_ra_e':
        dataset = CAIL2018(task_name='relevant_articles', sub_data='exercise')
    elif args.dataset == 'cal2018_ra_fs':
        dataset = CAIL2018(task_name='relevant_articles', sub_data='first_stage')
    elif args.dataset == 'cal2018_toi_e':
        dataset = CAIL2018(task_name='term_of_imprisonment', sub_data='exercise')
    elif args.dataset == 'cal2018_toi_fs_e':
        dataset = CAIL2018(task_name='term_of_imprisonment', sub_data='first_stage')
    else:
        raise '不支持的数据集'
    return dataset