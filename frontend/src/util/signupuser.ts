import type { FormEvent } from "react";
import type { NavigateFunction } from "react-router-dom";

export async function userSignup(
  e: FormEvent<HTMLFormElement>,
  username: string,
  email: string,
  password: string,
  setUsername: React.Dispatch<React.SetStateAction<string>>,
  setEmail: React.Dispatch<React.SetStateAction<string>>,
  setPassword: React.Dispatch<React.SetStateAction<string>>,
  setError: React.Dispatch<React.SetStateAction<string>>,
  setSuccess: React.Dispatch<React.SetStateAction<string>>,
  setLoading: React.Dispatch<React.SetStateAction<boolean>>,
  navigate: NavigateFunction,) {
  e.preventDefault();

  setError("");
  setSuccess("");
  setLoading(true);

  try {
    const response = await fetch("http://localhost:5050/api/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        email,
        password,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      setError(data.error || "Signup failed");
      return;
    }

    setSuccess("Account created successfully!");

    setUsername("");
    setEmail("");
    setPassword("");

    setTimeout(() => {
      navigate("/login");
    }, 1000);
  } catch (err) {
    setError("Could not connect to the backend");
  } finally {
    setLoading(false);
  }
}