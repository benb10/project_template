'use client';

import Image from 'next/image';
import React, { useEffect, useState } from 'react';

import { Api } from './api'; // Adjust the import path as needed

import styles from './page.module.css';

export default function Home() {
  const [title, setTitle] = useState<string>('');

  // Fetch the HelloWorld message on component mount
  useEffect(() => {
    const fetchTitle = async () => {
      try {
        const data = await Api.getHelloWorld();
        setTitle(data.message); // Set the message as title
      } catch (error) {
        console.error('Error loading hello world:', error);
        setTitle('Error loading title AA');
      }
    };

    fetchTitle();
  }, []); // Empty dependency array ensures it runs only once on mount

  return (
    <main className={styles.main}>
      <div className={styles.description}>
        {title}
        <p>
          Get started by editing&nbsp;
          <code className={styles.code}>src/app/page.tsx</code>
        </p>
        <div>
          <a href="https://vercel.com?utm_source=typescript-nextjs-starter" target="_blank" rel="noopener noreferrer">
            By{' '}
            <Image src="/vercel.svg" alt="Vercel Logo" className={styles.vercelLogo} width={100} height={24} priority />
          </a>
        </div>
      </div>

      <div className={styles.center}>
        <Image className={styles.logo} src="/next.svg" alt="Next.js Logo" width={180} height={37} priority />
      </div>

      <div className={styles.grid}>
        <a
          href="https://nextjs.org/docs?utm_source=typescript-nextjs-starter"
          className={styles.card}
          target="_blank"
          rel="noopener noreferrer"
        >
          <h2>
            Docs <span>-&gt;</span>
          </h2>
          <p>Find in-depth information about Next.js features and API.</p>
        </a>

        <a
          href="https://nextjs.org/learn?utm_source=typescript-nextjs-starter"
          className={styles.card}
          target="_blank"
          rel="noopener noreferrer"
        >
          <h2>
            Learn <span>-&gt;</span>
          </h2>
          <p>Learn about Next.js in an interactive course with&nbsp;quizzes!</p>
        </a>

        <a
          href="https://vercel.com/templates?framework=next.js&utm_source=typescript-nextjs-starter"
          className={styles.card}
          target="_blank"
          rel="noopener noreferrer"
        >
          <h2>
            Templates <span>-&gt;</span>
          </h2>
          <p>Explore the Next.js 13 playground.</p>
        </a>

        <a
          href="https://vercel.com/new?utm_source=typescript-nextjs-starter"
          className={styles.card}
          target="_blank"
          rel="noopener noreferrer"
        >
          <h2>
            Deploy <span>-&gt;</span>
          </h2>
          <p>Instantly deploy your Next.js site to a shareable URL with Vercel.</p>
        </a>
      </div>
    </main>
  );
}
