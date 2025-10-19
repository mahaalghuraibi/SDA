import { Routes, Route, Navigate } from 'react-router-dom';

return (
    <Routes>
        <Route path="/" element={<div>Home Page</div>} />
        <Route path="/login" element={<div>Login Page</div>} />
        {/* Redirect to /login if not authenticated when trying to access /dashboard */}
        <Route
            path="/dashboard"
            element={isAuthenticated ? <div>Dashboard</div> : <Navigate to="/login" replace />}
        />
        {/* Catch-all route for unmatched paths, redirects to home */}
        <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
);