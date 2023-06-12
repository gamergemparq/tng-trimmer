import configparser


def get_config_values():
    config = configparser.ConfigParser()
    config.read('config.ini')

    Config_values = {
        'source_file_name': config['DEFAULT']['source_file_name'],
        'output_file_name': config['DEFAULT']['output_file_name'],
        'lst_cols_to_keep': config['DEFAULT']['columns_to_keep'],
        'col_to_calc_sum': config['DEFAULT']['column_to_calc_sum'],

        'filter_col_name': config['FILTER']['column_name'],
        'filter_value_to_filter': config['FILTER']['value_to_filter']
    }

    return Config_values


def test_source_not_empty():
    config = get_config_values()
    assert len(config['source_file_name']) > 1 == True


def test_output_not_empty():
    config = get_config_values()
    assert len(config['output_file_name']) > 1 == True


def test_columns_to_keep_not_empty():
    config = get_config_values()
    assert len(config['lst_cols_to_keep']) > 1 == True


def test_column_to_calc_sum_not_empty():
    config = get_config_values()
    assert len(config['col_to_calc_sum']) > 1 == True
