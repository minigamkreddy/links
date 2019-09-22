https://github.com/AgarwalConsulting/learning-golang
https://github.com/Chennai-Golang




FROM GITHUB:
git clone https://github.com/jemcek/packETH.git
cd packETH
./autogen.sh (you will need aclocal,autoconf,autoheader and automake installed to run this)
autoreconf -f -i (optional if needed sometimes)
./configure
make
make install
./packETH

FROM SOURCEFORCE:
    1. 1)get the package from the DOWNLOAD page
    2. 2)unpack it: 
        tar xjvf packETH.x.y.tar.bz    (where x.y is the version you downloaded)
    3. 3)cd packETH
    4. 4)autoreconf -f -i (needed sometimes)
    5. 5)./configure
    6. 6)make 
    7. 7)make install   (optional)

Depending on your Linux distribution and type of installation additional packages may be needed. For example:

1) Centos 7.4 (minimal):
yum groupinstall 'Development Tools'
yum install gtk2-devel.x86_64

    2. 2)Ubuntu 18.04 server
sudo apt-get install build-essential
sudo apt-get install autoconf
sudo apt-get install pkg-config
sudo apt-get install gtk+2.0


LINUX PACKAGES (Ubuntu, Redhat, etc...): 
There are precompiled packages for many linux distribution available but normally they are not the latest versions. To install type as root or superuser:

Redhat, Centos: yum install packeth
Debian, Ubuntu: apt-get install packeth



mkdir Beaglebone
cd Beaglebone/
git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
cd linux/
make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/toolchain_blackbone/bin/arm-linux-gnueabi-  distclean
make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/toolchain_blackbone/bin/arm-linux-gnueabi-  multi_v7_defconfig
 make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/toolchain_blackbone/bin/arm-linux-gnueabi-

sudo make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/gcc-linaro-6.5.0-2018.12-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf- uImage dtbs LOADADDR=0x80008000 

git clone https://github.com/u-boot/u-boot
cd u-boot/
make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/gcc-linaro-6.5.0-2018.12-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf- distclean
make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/gcc-linaro-6.5.0-2018.12-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf- am335x_evm_config
make -j4 ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/gcc-linaro-6.5.0-2018.12-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-

cd linux/
sudo make ARCH=arm CROSS_COMPILE=/home/shaik/Beaglebone/gcc-linaro-6.5.0-2018.12-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf- -j4 modules
sudo make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- INSTALL_MOD_PATH=/media/shaik/f051490a-dd8d-4b33-963b-68bfcd8c385a/ modules_install


https://embedjournal.com/kernel-compilation-beaglebone-black/
https://elinux.org/Building_BBB_Kernel
https://embedjournal.com/kernel-compilation-beaglebone-black/
https://longervision.github.io/2018/01/10/Embedded/beaglebone-black-uboot-kernel/
http://www.bootembedded.com/embedded-linux/building-embedded-linux-scratch-beaglebone-black/




DOCKER LINKS

https://www.katacoda.com/courses/docker/deploying-first-container
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
https://hub.docker.com/
https://www.katacoda.com/javajon/courses/kubernetes-fundamentals/minikube
https://kubernetes.io/
https://www.edureka.co/blog/install-kubernetes-on-ubuntu
https://www.virtualbox.org/wiki/Downloads
https://www.osboxes.org/ubuntu/
https://sourceforge.net/projects/osboxes/
katacoda minikube
katacoda docker
https://static.brandonpotter.com/kurbernetes/DeploymentBuilder.html
https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/
https://kubernetes.io/docs/tutorials/stateless-application/guestbook/



go get -u github.com/urfave/negroni 
go get -u github.com/golang/dep/cmd/dep
https://www.gorillatoolkit.org/pkg/mux
https://github.com/Chennai-Golang/101-workshop/blob/master/Setup.md
https://github.com/AgarwalConsulting/learning-golang/blob/master/004-http-application/003-handler-interface.go
https://tour.golang.org/moretypes/4
https://github.com/sirupsen/logrus
https://12factor.net/
https://github.com/golang-standards/project-layout

To compile the go folders in the garnet

Example

/.goenv/src/github.com/Chennai-Golang/101-workshop/examples/packages
vi hello.go
go build .
./packages

http://gorm.io/docs/models.html
https://golang.org/src/unsafe/unsafe.go

examples on channels
https://tour.golang.org/concurrency/5

timer := time.After
(time.Microsecond * 10) <- timer
quit <- 0

golang.org/pkg/builtin

https://tour.golang.org/garbagecollector/1
https://github.com/go-ozzo/ozzo-validation



https://blog.golang.org/using-go-modules

Garbage Collector

GoTri-colour concurrent mark and sweep garbage collector

Python uses GC and ARC (Automatic Reference Coding)

GO 

1) Mark phase
2) Sweep phases

Go uses the breathefirst traversing (depthfirst)

https://golang.org/pkg/runtime/

1) Latency: low latency
2) Throughput : how many operations can program can do
high Throughput

https://making.pusher.com/golangs-real-time-gc-in-theory-and-practice/
https://making.pusher.com/go-tool-trace/
https://github.com/WillSewell/gc-latency-experiment


GOMAXPROCS controls no of go routines

goenv version


go get -u github.com/google/pprof
pprof mem.prof
pprof -http localhost:9001 cpu.prof
apt-get install graphviz

https://golang.org/pkg/net/http/pprof/
https://github.com/WillSewell/gc-latency-experiment


To control the race condition in golang

go run -race main.go

GOMAXPROC=2 make run-go-preemption

gomega
ginkgo

https://onsi.github.io/ginkgo/
https://golang.org/pkg/runtime/debug/
https://golang.org/pkg/context/


docker build -t  books-example:latest .
Docker run -it -p 9000:9000 books-examples:latest





