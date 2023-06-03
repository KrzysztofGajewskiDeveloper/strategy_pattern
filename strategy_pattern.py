from typing import Callable
from functools import partial
from dataclasses import dataclass, field
import os


ReportSaverStrategy = Callable[[str], None]


def save_as_csv(data: str, file_path: str, delimiter: str) -> None:
    file_path: str = f'{file_path}.csv'
    print(f'CSV report saved in: {file_path} with {delimiter=}\n')


def save_as_pdf(data: str, file_path: str, encryption: bool) -> None:
    file_path: str = f'{file_path}.pdf'
    print(f'PDF report saved in: {file_path} \n{encryption=}\n')


@dataclass
class OnlineResearcher:
    directory: str
    reports: dict[str, str] = field(default_factory=dict)

    def search_for(self, text: str):
        print(f'online research regarding "{text}" conducted')
        self.reports[text] = f'{text} report'

    def save_report(self, report: str, save_as: ReportSaverStrategy) -> None:
        file_path: str = os.path.join(self.directory, report)
        data: str = self.reports[report]
        save_as(data, file_path)


def main():
    comma_csv_strategy: ReportSaverStrategy = partial(save_as_csv, delimiter=',')
    encrypted_pdf_strategy: ReportSaverStrategy = partial(save_as_pdf, encryption=True)
    decrypted_pdf_strategy: ReportSaverStrategy = partial(save_as_pdf, encryption=False)

    researcher: OnlineResearcher = OnlineResearcher(directory='c:/')

    animals: dict[str, ReportSaverStrategy] = {
        'duck': comma_csv_strategy,
        'cat': encrypted_pdf_strategy,
        'dog': decrypted_pdf_strategy,
        'donkey': comma_csv_strategy}

    for animal, save_as_strategy in animals.items():
        researcher.search_for(animal)
        researcher.save_report(animal, save_as_strategy)


if __name__ == "__main__":
    main()
