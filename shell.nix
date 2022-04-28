{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  name = "python3-pip";

  #
  # May be required:
  #
  # pip install setuptools
  # pip install wheel
  #

  nativeBuildInputs = with pkgs; [
    python310
    twine
  ];
}
