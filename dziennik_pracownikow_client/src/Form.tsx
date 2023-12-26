import { FormEvent, Fragment, useState } from "react";
import { startEndWork } from "./api/EmployeeApi";
import { Input } from "./components/Input";
import "./styles/App.css";

const Form = () => {
	const [error, setError] = useState("");
	const [helperText, setHelperText] = useState("");
	const [pin, setPin] = useState("");
	const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		setError("");
		setHelperText("");
		const response = await startEndWork(pin);
		if (!response.success) {
			setError(response.message);
			return;
		}
		setHelperText(response.message);
		return;
	};
	return (
		<Fragment>
			<form className="card" onSubmit={handleSubmit}>
				<h3>Work schedule</h3>
				<Input
					value={pin}
					onChange={setPin}
					label="PIN"
					maxLength={6}
					minLength={4}
					type="text"
					error={!!error}
					helperText={error ? error : helperText}
					required
				/>
				<button>Log in</button>
			</form>
		</Fragment>
	);
};

export default Form;
