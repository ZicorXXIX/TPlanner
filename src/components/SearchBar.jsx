import React from 'react';

export default function SearchBar() {
  return (
    <div className="max-w-lg mx-auto">
      <input
        type="text"
        placeholder="Search..."
        className="px-3 py-1 w-full border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 rounded-md"
      />
    </div>
  );
}
