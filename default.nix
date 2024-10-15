{ lib
, buildPythonPackage
, fetchFromGitHub
, pretix-plugin-build
, setuptools
, xsdata
, requests
}:

buildPythonPackage rec {
  pname = "pretix-szamlazz";
  version = "0.0.1";
  pyproject = true;

  src = ./.;

  build-system = [
    pretix-plugin-build
    setuptools
  ];

  dependencies = [
    xsdata
    requests
  ];

  doCheck = false; # no tests

  pythonImportsCheck = [
    "pretix_szamlazz"
  ];
}