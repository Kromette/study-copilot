import hashlib
from pathlib import Path


def compute_file_hash(
    file_path: Path,
) -> str:
    """
    Compute SHA256 hash of a file.

    Same file content = same hash.
    """

    sha256 = hashlib.sha256()

    with open(
        file_path,
        "rb"
    ) as file:

        for chunk in iter(
            lambda: file.read(4096),
            b"",
        ):

            sha256.update(chunk)


    return sha256.hexdigest()