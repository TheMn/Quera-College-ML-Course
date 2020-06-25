class Table:
    def __init__(self, path=None):
        self.labels = []
        self.rows = []
        if path is not None:
            with open(path, "r+") as file:
                first_line = True
                for line in file:
                    line = line.rstrip('\n')
                    if first_line:
                        first_line = False
                        self.labels = line.split(",")
                    else:
                        self.rows.append(line.split(","))
                contents = file.read()

    def save(self, path):
        with open(path, "w") as file:
            file.writelines(",".join(self.labels) + '\n')
            for row in self.rows:
                file.writelines(",".join(row) + '\n')

    def get_row_dict(self, row_index):
        return {
            self.labels[i]: x for i, x in enumerate(self.rows[row_index])
        }

    def get_cell(self, row_index, label):
        return self.rows[row_index][self.labels.index(label)]

    def get_column(self, label):
        return [x[self.labels.index(label)] for x in self.rows]

    def get_label_index(self, label):
        if label in self.labels:
            return self.labels.index(label)
        else:
            raise KeyError("haji nadarim az ina")

    def to_dict(self):
        return {
            "labels": self.labels,
            "rows": self.rows
        }
