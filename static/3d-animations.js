// Loads and displays a 3D GLB model using Three.js and GLTFLoader via CDN
// Make sure to add a <div id="laptop-3d-canvas"></div> in your HTML where you want the model

document.addEventListener('DOMContentLoaded', function() {
	const canvasContainer = document.getElementById('laptop-3d-canvas');
	if (!canvasContainer) return;

	// Scene setup
	const scene = new THREE.Scene();
	scene.background = new THREE.Color(0xeef3f8);

	const camera = new THREE.PerspectiveCamera(35, canvasContainer.offsetWidth / canvasContainer.offsetHeight, 0.1, 1000);
	camera.position.set(0, 1.2, 3.5);

	const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
	renderer.setSize(canvasContainer.offsetWidth, canvasContainer.offsetHeight);
	canvasContainer.appendChild(renderer.domElement);

	// Lighting
	const ambientLight = new THREE.AmbientLight(0xffffff, 1.1);
	scene.add(ambientLight);
	const directionalLight = new THREE.DirectionalLight(0xffffff, 0.7);
	directionalLight.position.set(2, 5, 5);
	scene.add(directionalLight);

	// Load GLB model
	const loader = new THREE.GLTFLoader();
	loader.load('/static/laptop.glb', function(gltf) {
		const model = gltf.scene;
		model.position.set(0, -0.5, 0);
		model.rotation.y = Math.PI / 6;
		model.scale.set(1.5, 1.5, 1.5);
		scene.add(model);

		// Animate model (slow rotation)
		function animate() {
			requestAnimationFrame(animate);
			model.rotation.y += 0.003;
			renderer.render(scene, camera);
		}
		animate();
	}, undefined, function(error) {
		console.error('Error loading GLB:', error);
	});
});