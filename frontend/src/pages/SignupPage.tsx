import { useState } from "react";
import Banner from "../components/Banner";
import { Link, useNavigate } from "react-router-dom";
import { userSignup } from "../util/signupuser";
import type { FormEvent } from "react";

function SignupPage() {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSignup = (e: FormEvent<HTMLFormElement>) => {
    userSignup(
      e,
      username,
      email,
      password,
      setUsername,
      setEmail,
      setPassword,
      setError,
      setSuccess,
      setLoading,
      navigate
    );
  };

  return (
    <>
      <Banner />
      <div className="auth-page">
        <div className="auth-card">
          <h1>Create Account</h1>
          <p>Sign up for DarkHorse Sports</p>

          <form onSubmit={handleSignup} className="auth-form">
            <input
              type="text"
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />

            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />

            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />

            <button type="submit" disabled={loading}>
              {loading ? "Creating Account..." : "Sign Up"}
            </button>
          </form>

          {error && <p className="auth-error">{error}</p>}
          {success && <p className="auth-success">{success}</p>}

          <p className="auth-switch">
            Already have an account? <Link to="/login">Log in</Link>
          </p>
        </div>
      </div>
    </>
  );
}

export default SignupPage;
