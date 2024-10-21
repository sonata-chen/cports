pkgname = "carla"
pkgver = "2.5.9_git20241001"
pkgrel = 0
_gitrev = "e312817b6f3d95e928dfde119934e7657092e7cc"
build_style = "makefile"
hostmakedepends = [
    "gmake",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "chimerautils-devel",
    "file-devel",
    "fluidsynth-devel",
    "liblo-devel",
    "libpulse-devel",
    "libsndfile-devel",
    "python-pyqt6",
    "qt6-qtbase-devel",
]
pkgdesc = "Audio plugin host"
maintainer = "sonata-chen <example@mail.com>"
license = "GPL-2.0-or-later"
url = "https://kx.studio/Applications:Carla"
source = f"https://github.com/falkTX/Carla/archive/{_gitrev}.zip"
sha256 = "448884236b258871ba964a8179c43bd8d287536543fd5f9f999540f4c0a329fb"
tool_flags = {"LDFLAGS": ["-lfts"]}

# no tests
options = ["!check"]
# crashes in test_src_input_decoder
hardening = ["!int"]
