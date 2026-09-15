// MarqueeRow.jsx — fila infinita en loop horizontal.
// Deps: framer-motion. Uso: <MarqueeRow speed={20}><span>BIO</span>...</MarqueeRow>. Requiere Tailwind.
import { Children } from "react";
import { motion } from "framer-motion";

export default function MarqueeRow({ children, speed = 24 }) {
  const items = Children.toArray(children);
  return (
    <div className="relative flex w-full overflow-hidden">
      <motion.div
        className="flex shrink-0 gap-8 pr-8"
        animate={{ x: ["0%", "-50%"] }}
        transition={{ duration: speed, ease: "linear", repeat: Infinity }}
      >
        {items}
        {items}
      </motion.div>
    </div>
  );
}
