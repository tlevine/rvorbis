with import <nixpkgs> {}; {
  rvorbisEnv = stdenv.mkDerivation {
    name = "rvorbis";
    buildInputs = [ libvorbis ];
    LIBRARY_PATH="${libvorbis}/lib";
  };  
}
