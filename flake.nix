{
  description = "A simple flake providing a Python environment with arrow and icalendar packages";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:

  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
    pythonEnv = pkgs.python39.withPackages (ps: with ps; [
      arrow
      icalendar
    ]);
  in
  {
    defaultPackage.${system} = pythonEnv;

    devShell.${system} = pkgs.mkShell {
      buildInputs = [
        pythonEnv
      ];
    };
  };
}
