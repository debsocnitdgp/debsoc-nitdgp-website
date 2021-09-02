$("#menu").on("mouseenter", function() {

    $("#menu").addClass('hovered');


})

$("#menu").on("mouseleave", function() {

    $("#menu").removeClass('hovered');


})

var scene, camera, renderer, stars, starGeo, controls;
var mouseX = 0,
    mouseY = 0;
var windowHalfX = window.innerWidth / 2;
var windowHalfY = window.innerHeight / 2;


function init() {

    scene = new THREE.Scene();

    camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);
    camera.position.set(0, 0, 1);
    camera.rotation.x = Math.PI / 2;


    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    controls = new THREE.OrbitControls(camera, renderer.domElement);
    camera.rotation.x = Math.PI / 2;
    controls.enablePan = false;

    controls.minDistance = 150;
    controls.maxDistance = 200;
    controls.screenSpacePanning = false;
    //controls.maxPolarAngle = 1.5;
    //controls.minPolarAngle = 1.0;
    //controls.maxAzimuthAngle = 0.4;
    //controls.minAzimuthAngle = -0.4;

    starGeo = new THREE.Geometry();
    for (let i = 0; i < 4000; i++) {
        star = new THREE.Vector3(
            Math.random() * 600 - 300,
            Math.random() * 600 - 300,
            Math.random() * 600 - 300
        );
        star.velocity = 0.002;
        star.acceleration = 0.002;
        starGeo.vertices.push(star);
    }

    let sprite = new THREE.TextureLoader().load('http://debsocnitdgp.in/static/star.png');
    let starMaterial = new THREE.PointsMaterial({
        color: 0xaaaaaa,
        size: 0.7,
        map: sprite
    });

    stars = new THREE.Points(starGeo, starMaterial);
    scene.add(stars);

    document.addEventListener('mousemove', onDocumentMouseMove, false);
    document.addEventListener('touchstart', onDocumentTouchStart, false);
    document.addEventListener('touchmove', onDocumentTouchMove, false);

    window.addEventListener("resize", onWindowResize, false);

    animate();
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;

    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function onDocumentMouseMove(event) {

    mouseX = event.clientX - windowHalfX;
    mouseY = event.clientY - windowHalfY;

}

function onDocumentTouchStart(event) {

    if (event.touches.length > 1) {

        event.preventDefault();

        mouseX = event.touches[0].pageX - windowHalfX;
        mouseY = event.touches[0].pageY - windowHalfY;

    }

}

function onDocumentTouchMove(event) {

    if (event.touches.length == 1) {

        event.preventDefault();

        mouseX = event.touches[0].pageX - windowHalfX;
        mouseY = event.touches[0].pageY - windowHalfY;

    }

}

function animate() {
    starGeo.vertices.forEach(p => {
        //p.velocity += p.acceleration
        p.y -= p.velocity;

        if (p.y < -200) {
            p.y = 200;
            p.velocity = 0;
        }
    });
    starGeo.verticesNeedUpdate = true;
    stars.rotation.y += 0.002;
    stars.rotation.x += 0.002;
    //renderer.render(scene, camera);
    requestAnimationFrame(animate);
    controls.update();
    render();
}

function render() {

    camera.position.x += (mouseX - camera.position.x) * 0.0025;
    camera.position.y += (mouseY - camera.position.y) * 0.003;

    //camera.lookAt( scene.position );
    //pivotPoint.rotation.y += 0.01;
    renderer.render(scene, camera);

}
init();