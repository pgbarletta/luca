from pathlib import Path
from attrs import define, field
from primitives import FileHandle


@define
class Complex:
    """
    Class that represents the simulated complex.
    """

    file_path: Path = field(converter=Path)
    name: str = field(converter=str)
    gro_file: FileHandle = field(init=False)
    pdb_file: FileHandle = field(init=False)
    top_name: str = field(kw_only=True, default="topol.top")
    top_file: FileHandle = field(init=False)

    def __attrs_post_init__(self):
        self.gro_file = FileHandle(Path.joinpath(self.file_path, self.name + ".gro"))
        self.pdb_file = FileHandle(Path.joinpath(self.file_path, self.name + ".pdb"))
        self.top_file = FileHandle(Path.joinpath(self.file_path, self.top_name))
