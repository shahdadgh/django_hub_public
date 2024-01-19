"use client";
// Import necessary modules from Next.js and React
import { useRouter } from 'next/navigation';
import React from 'react';

export default function Page() {
  // return (
  // useRouter hook for client-side navigation
  const router = useRouter();

  // Function to handle the button click and navigate to /page2
  const navigateToPage2 = () => {
    router.push('/page2');
  };

  return (
    <div>
      <h1>Welcome to Page 1</h1>
      <button onClick={navigateToPage2}>Go to Page 2</button>
    </div>
  );
};

// export default Page;
