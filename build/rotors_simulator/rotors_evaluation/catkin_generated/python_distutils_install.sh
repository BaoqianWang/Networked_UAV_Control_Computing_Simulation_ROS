#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/smile/nac_sim/src/rotors_simulator/rotors_evaluation"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/smile/nac_sim/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/smile/nac_sim/install/lib/python2.7/dist-packages:/home/smile/nac_sim/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/smile/nac_sim/build" \
    "/usr/bin/python2" \
    "/home/smile/nac_sim/src/rotors_simulator/rotors_evaluation/setup.py" \
     \
    build --build-base "/home/smile/nac_sim/build/rotors_simulator/rotors_evaluation" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/smile/nac_sim/install" --install-scripts="/home/smile/nac_sim/install/bin"
