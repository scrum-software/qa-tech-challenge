
class TableToDictionary:
    def __init__(self):
        self.cell_values_object = {}

    def convert_table_to_dict(self, table):
        for row_number, table_row in enumerate(table):
            row_name = self.add_row_to_dict(row_number)
            self.add_cells_to_dict(row_name, table_row.row_cells)

        return self.cell_values_object

    def add_row_to_dict(self, row_number):
        row_name = 'Row {}'.format(row_number)
        self.cell_values_object.update({row_name: []})
        return row_name

    def add_cells_to_dict(self, row_name, row_cells):
        for row_cell in row_cells:
            self.cell_values_object[row_name].append(row_cell.cell_value)


class ListParser:
    @staticmethod
    def indexate_list_sums(list_of_integers):
        total_list_count = 0
        list_calculation_indices = []

        for list_item in list_of_integers:
            total_list_count += list_item
            list_calculation_indices.append(total_list_count)

        return list_calculation_indices

    @staticmethod
    def derive_central_list_index(indexed_list_original, indexed_list_inverted):
        for idx, list_item in enumerate(indexed_list_original):
            if list_item in indexed_list_inverted:
                # According to the specification, we want to return "human-readable" index, which starts at 1.
                # Also, the specification asks for only the first result, even if multiple are available.
                return idx + 1
        return None

    def derive_answers(self, cell_values_object):
        completed_answers = []

        for list_original in cell_values_object.values():
            list_inverted = list_original[::-1]
            indexed_list_original = self.indexate_list_sums(list_original)
            indexed_list_inverted = self.indexate_list_sums(list_inverted)
            completed_answers.append(
                self.derive_central_list_index(indexed_list_original, indexed_list_inverted))

        return completed_answers
