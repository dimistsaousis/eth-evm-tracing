use anyhow::{anyhow, Result};
use cfmms::{
    checkpoint::sync_pools_from_checkpoint,
    dex::{Dex, DexVariant},
    pool::Pool,
    sync::sync_pairs,
};
use dashmap::DashMap;
use ethers::{
    abi,
    providers::{Provider, Ws},
    types::{Address, BlockNumber, Diff, TraceType, Transaction, H160, H256, U256, U64},
    utils::keccak256,
};
use ethers_providers::Middleware;
use log::info;
use std::{path::Path, str::FromStr, sync::Arc};
use tokio::sync::broadcast::{self, Sender};
use tokio::task::JoinSet;
use tokio_stream::StreamExt;

use crate::utils::calculate_next_block_base_fee;

// Create this function first
pub async fn mempool_watching(target_address: String) -> Result<()> {
    // Setup: Create the WS provider and wrap it in Arc
    let wss_url: String = std::env::var("WSS_URL").unwrap();
    let provider = Provider::<Ws>::connect(wss_url).await?;
    let provider = Arc::new(provider);
}