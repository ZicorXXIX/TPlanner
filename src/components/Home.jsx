import React from "react";
import SearchBar from "./SearchBar";

export default function Home() {
    return (
  
      <div className="flex flex-col items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-md mx-auto space-y-12">
          <h2 className="text-3xl leading-9 font-extrabold tracking-tight text-gray-900 sm:text-4xl sm:leading-10">
            The best place to buy and sell used cars
          </h2>
          <p className="mt-3 text-base leading-6 text-gray-500 sm:mt-4 sm:text-lg sm:leading-7">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quibusdam.
          </p>
          <SearchBar/>          
          
          <div className="mt-8 flex justify-center">
            <div className="rounded-md shadow">
              <a
                href="#"
                className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base leading-6 font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-500 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700 transition duration-150 ease-in-out"
              >
                Learn more
              </a>
            </div>
            <div className="ml-3 rounded-md shadow">
              <a
                href="#"
                className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base leading-6 font-medium rounded-md text-indigo-600 bg-white hover:text-indigo-500 focus:outline-none focus:border-indigo-300 focus:shadow-outline-indigo active:text-indigo-700 active:bg-indigo-100 transition duration-150 ease-in-out"
              >
                Learn more
              </a>
            </div>
          </div>
        </div>
      </div>
      
    
    );
  }
    
  
  