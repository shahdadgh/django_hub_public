"use client";
// Import necessary modules from Next.js and React
import { useRouter } from 'next/navigation';
import React from 'react';

export default function Page2() {
  // return (
  // useRouter hook for client-side navigation
  const router = useRouter();

  // Function to handle the button click and navigate to /page2
  const navigateToHome = () => {
    router.push('/');
  };

  return (
    <div>
      <h1>Welcome to Page 1</h1>
      <button onClick={navigateToHome}>Go to app3 Home Page</button>
    </div>
  );
};

// export default Page;
