
class TableToDictionary:
    def __init__(self):
        self.completed_count_dict = {}

    def convert_table_to_dict(self, table):
        for row_number, table_row in enumerate(table):
            row_name = self.add_row_to_dict(row_number)
            self.add_cells_to_dict(row_name, table_row.row_cells)

        return self.completed_count_dict

    def add_row_to_dict(self, row_number):
        row_name = 'Row {}'.format(row_number)
        self.completed_count_dict.update({row_name: []})
        return row_name

    def add_cells_to_dict(self, row_name, row_cells):
        for row_cell in row_cells:
            self.completed_count_dict[row_name].append(row_cell.cell_value)


class ArrayParser:
    def equalise_array(self, array):

