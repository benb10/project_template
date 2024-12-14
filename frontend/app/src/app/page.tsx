"use client";

import Image from "next/image";
import React, { useEffect, useState } from "react";

import Api from "./api";

import styles from "./page.module.css";

export default function Home() {
	const [title, setTitle] = useState<string>("");

	// Fetch the HelloWorld message on component mount
	useEffect(() => {
		const fetchTitle = async () => {
			try {
				const data = await Api.getHelloWorld();
				setTitle(data.message); // Set the message as title
			} catch (error) {
				console.error("Error loading hello world:", error);
				setTitle("Error loading title");
			}
		};

		fetchTitle();
	}, []); // Empty dependency array ensures it runs only once on mount

	return (
		<main className={styles.main}>
			<div className={styles.description}>
				{title}
				backend url: {process.env.NEXT_PUBLIC_API_URL}
				<br />
				version: 3
				<p>
					Get started by editing&nbsp;
					<code className={styles.code}>src/app/page.tsx</code>
				</p>
				<div>
					<a
						href="https://vercel.com?utm_source=typescript-nextjs-starter"
						target="_blank"
						rel="noopener noreferrer"
					>
						By{" "}
						<Image
							src="/vercel.svg"
							alt="Vercel Logo"
							className={styles.vercelLogo}
							width={100}
							height={24}
							priority
						/>
					</a>
				</div>
			</div>

			<div className={styles.center}>
				<Image
					className={styles.logo}
					src="/next.svg"
					alt="Next.js Logo"
					width={180}
					height={37}
					priority
				/>
			</div>

			<div className={styles.grid}>

			</div>
		</main>
	);
}
