{ pkgs }: {
  deps = [
    pkgs.glibcLocales
    pkgs.glibc
    pkgs.systemdStage1Network
    pkgs.lsof /nix/store/6a58h0n1gzxzgfi5d0n8az0dizzwpyg7-util-linux-2.37.2-bin
    pkgs.ewrgewrg
  ];
}