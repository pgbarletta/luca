from pathlib import Path
from attrs import define, field


@define
class FileHandle:
    path: Path = field(converter=Path)
    new: bool = field(kw_only=True, default=False)
    name: str = field(init=False)
    extension: str = field(init=False)

    @path.validator
    def file_exists(self, attribute, value):
        if not self.new and not value.is_file():
            raise ValueError(f"File: {value} doesn't exist.")

    def __attrs_post_init__(self):
        try:
            self.name, self.extension = self.path.name.split(".")
        except Exception as e:
            raise e(f"Bad input for FileHandle: {self.path}")
