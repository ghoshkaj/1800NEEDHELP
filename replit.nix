{ pkgs }: {
  deps = [
    pkgs.postgresql
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.nodejs-18_x
    pkgs.nodePackages.npm
  ];
} 