import { employeeRouter, serverUrl } from "./serverUrl";

type ResponseType = {
	message: string;
	success: boolean;
};

export const startEndWork = async (pin: string) => {
	return await fetch(`${serverUrl}${employeeRouter}start-end-work/${pin}`)
		.then((res) => res.json())
		.then((data: ResponseType) => data);
};
