{
  description = "A simple flake providing a Python environment with arrow and icalendar packages";

  inputs = {
    nixpkgs.url = github:nixos/nixpkgs/nixos-22.11;
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
        name = "calendar";
        buildInputs = [
          pythonEnv
          pkgs.zsh
        ];

        postShellHook = ''
			zsh
			'';

      };
    };
}
