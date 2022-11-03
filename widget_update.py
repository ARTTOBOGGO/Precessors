

class Configure_widgets:

    def configure_cpu_bar(self):

        r = self.cpu.cpu_percent_return()

        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f'core{i+1} usage:{r[i]}%')
            self.list_pbar[i].configure(value=r[i])
