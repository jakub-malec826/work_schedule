import { Fragment, InputHTMLAttributes, useMemo, useState } from "react";
import "../styles/Input.css";

type InputParams = { label: string; error?: boolean; helperText?: string; onChange?: (input: string) => void } & Omit<
	InputHTMLAttributes<HTMLInputElement>,
	"id" | "onChange" | "onFocus" | "onBlur"
>;

export const Input = ({ label, error, helperText, value: valueFromProps, onChange, ...props }: InputParams) => {
	const id = useMemo(() => "_" + Math.random().toString(16).slice(6), []);

	const [value, setValue] = useState(valueFromProps);
	const [className, setClassName] = useState("input");

	return (
		<Fragment>
			<div className="input__group">
				<input
					className={className}
					id={id}
					value={value}
					onChange={(e) => {
						setValue(e.target.value);
						onChange && onChange(e.target.value);
					}}
					onFocus={() => setClassName("input-focused")}
					onBlur={() => value === "" && setClassName("input")}
					{...props}
				/>
				<label className="input__label" htmlFor={id}>
					{label}
				</label>
			</div>
			{!!helperText && <label className={error ? "input__error" : "input__helperText"}>{helperText}</label>}
		</Fragment>
	);
};
