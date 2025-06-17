from flask import Flask, render_template, request
from quantum_login import quantum_login_simulation
from server_quantum import server_apply_corrections

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        b0, b1 = quantum_login_simulation()
        q2_state = server_apply_corrections(b0, b1)
        state_vector = q2_state.data.flatten()
        state_str = f"{state_vector[0]:.2f} |0⟩ + {state_vector[1]:.2f} |1⟩"
        return render_template("login.html", b0=b0, b1=b1, state=state_str, success=True)

    return render_template("login.html", success=False)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
