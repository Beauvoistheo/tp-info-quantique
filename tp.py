from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit_ibm_runtime import QiskitRuntimeService, Estimator

# Connexion au service IBM Quantum
service = QiskitRuntimeService()
backend = service.backend("ibmq_qasm_simulator")

# Initialisation de l'Estimator
estimator = Estimator(options={'backend': backend})
estimator.options.resilience_level = 1
estimator.options.default_shots = 5000

# Exemple de circuitpython -m qiskit_ibm_runtime.account save --token VOTRE_TOKEN_IBM

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Observable pour la mesure
observable = SparsePauliOp.from_list([("ZZ", 1)])
mapped_observables = [observable]

# Lancer le job
job = estimator.run([(qc, mapped_observables)])

# Récupérer l'ID du job
print(f">>> Job ID: {job.job_id()}")
